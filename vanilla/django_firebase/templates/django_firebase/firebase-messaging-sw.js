importScripts("https://www.gstatic.com/firebasejs/11.3.0/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/11.3.0/firebase-messaging-compat.js");
const SW_VERSION = '0.0.15';

//self.addEventListener("install", (event) => {
//    event.waitUntil(
//        fetch("/firebase/config/", {credentials: "include"})  // Fetch the config from Django
//            .then(response => response.json())
//            .then(firebaseConfig => {
//                firebase.initializeApp(firebaseConfig); // Initialize Firebase with dynamic config
//                console.log(`🔥 Firebase Service Worker Activated - Version: ${SW_VERSION}`);
//            })
//            .catch(error => console.error("❌ Error fetching Firebase config:", error))
//    );
//});


const firebaseConfig = {{ FIREBASE_CONFIG|safe }};

// Initialize Firebase
self.addEventListener("install", (event) => {
    firebase.initializeApp(firebaseConfig)
    console.log(`🔥 Firebase Service Worker Activated - Version: ${SW_VERSION}`);
});


// Initialize messaging after fetching config
self.addEventListener("activate", () => {
    if (firebase.apps.length > 0) {
        const messaging = firebase.messaging();

        messaging.onBackgroundMessage((payload) => {
            console.log("📩 Background received  message", payload);
            const notificationTitle = payload.data.title;
            const notificationOptions = {
                body: payload.data.body,
                icon: payload.data.image,
                data: { url: payload.data.click_action},
            };
            return self.registration.showNotification(notificationTitle, notificationOptions);
        });
    } else {
        console.error("🚨 Firebase not initialized.");
    }
});



self.addEventListener("notificationclick", (event) => {
    console.log("🔗 Notification clicked:", event);
    event.notification.close();

    const urlToOpen = event.notification.data.url;

    event.waitUntil(
        clients.matchAll({ type: "window", includeUncontrolled: true }).then((windowClients) => {
            for (let client of windowClients) {
                if (client.url === urlToOpen && "focus" in client) {
                    return client.focus();
                }
            }
            if (clients.openWindow) {
                return clients.openWindow(urlToOpen);
            }
        })
    );
});