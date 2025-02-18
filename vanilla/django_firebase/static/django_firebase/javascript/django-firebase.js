// THIS IS A LOCAL COPY THAT SHOULD BE IN THE STATICS DIR BUT IT WASN'T CREATED FOR THIS PROJECTS (S3 ONLY)
//

// Fetch Firebase config from the backend
const SW_VERSION = '1.0.13';

fetch("/django_firebase/config/")
    .then(response => response.json())
    .then(config => {
        console.log("Fetched Firebase Config:", config, SW_VERSION);

        // Initialize Firebase with the retrieved config
        firebase.initializeApp(config);

        // Initialize Firebase Messaging
        const messaging = firebase.messaging();
        console.log('messaging', messaging);

        function requestPushPermission() {
            if (Notification.permission === 'default') {
                Notification.requestPermission().then(function(permission) {
                    if (permission === "granted") {
                        console.log("Notification permission granted.");
                        getPushToken();
                    } else {
                        console.log("Notification permission denied.");
                    }
                });
            } else {
                console.log('Permission already set:', Notification.permission);
                getPushToken();
            }
        }

        function getPushToken() {
            messaging.getToken({ vapidKey: config.vapidKey })
                .then(function(currentToken) {
                    if (currentToken) {
                        console.log("FCM Token:", currentToken);
                        const storedToken = localStorage.getItem('fcm_push_token') || 'not found';
                        if(storedToken !== currentToken){
                            localStorage.setItem('fcm_push_token', currentToken);
                            sendTokenToServer(currentToken, storedToken);
                        }
                    } else {
                        console.log("No FCM token available.");
                    }
                })
                .catch(function(err) {
                    console.error("Error retrieving FCM token:", err);
                });
        }

        function getCSRFTokenFromDOM() {
            return document.querySelector('input[name="csrfmiddlewaretoken"]')?.value;
        }

        function sendTokenToServer(token, storedToken) {
            fetch('/django_firebase/register-web-push/', {
                method: 'POST',
                body: new URLSearchParams({
                    new_token: token,
                    previous_token: storedToken
                }),
                headers: {
                    "X-CSRFToken": getCSRFTokenFromDOM(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }).then(response => response.json())
              .then(data => console.log("Token sent to server:", data))
              .catch(error => console.error("Error sending token to server:", error));
        }

        messaging.onMessage((payload) => {
            console.log("📩 Foreground message received:", payload);

            const notificationTitle = payload.data.title;
            const notificationOptions = {
                body: payload.data.body,
                icon: payload.data.image,
                data: { url: payload.data?.click_action || config.defaultDest }
            };

            const notification = new Notification(notificationTitle, notificationOptions);

            notification.onclick = (event) => {
                event.preventDefault();
                window.open(notificationOptions.data.url, "_blank");
            };
        });

        // Init push request check
        requestPushPermission();

    })
    .catch(error => console.error("Error fetching Firebase config:", error));
