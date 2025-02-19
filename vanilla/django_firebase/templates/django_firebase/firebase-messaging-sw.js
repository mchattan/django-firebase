importScripts("https://www.gstatic.com/firebasejs/11.3.0/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/11.3.0/firebase-messaging-compat.js");

const SW_VERSION = '0.0.25';
console.log(`🛠️ Service Worker Loading - Version: ${SW_VERSION}`);

let messaging = null;

// Firebase config needs to be embedded at build time or fetched dynamically
const firebaseConfig = {
    apiKey: "{{ apiKey }}",
    authDomain: "{{ authDomain }}",
    projectId: "{{ projectId }}",
    storageBucket: "{{ storageBucket }}",
    messagingSenderId: "{{ messagingSenderId }}",
    appId: "{{ appId }}"
};

// Initialize Firebase only if it's not already initialized
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
    messaging = firebase.messaging();
    console.log("🔥 Firebase Messaging initialized.");
} else {
    console.log("⚠️ Firebase app already initialized.");
}

// Ensure `push` event is registered immediately
self.addEventListener("push", (event) => {
    console.log("📩 Push event received.");

    if (!messaging) {
        console.error("🚨 Firebase Messaging not initialized in push event.");
        return;
    }

    const payload = event.data ? event.data.json() : {};
    console.log("📨 Push payload:", payload);

    const notificationTitle = payload.data.title;
    const notificationOptions = {
        body: payload.data.body,
        icon: payload.data.image,
        data: { url: payload.data.click_action},
    };

//    const notificationOptions = {
//        body: payload.data?.body || "You have a new message.",
//        icon: payload.data?.icon || "/default-icon.png",
//        data: { url: payload.data?.click_action || "/" },
//    };

    event.waitUntil(self.registration.showNotification(notificationTitle, notificationOptions));
});

// Handle notification click
self.addEventListener("notificationclick", (event) => {
    console.log("🔗 Notification clicked:", event);
    event.notification.close();

    const urlToOpen = event.notification.data.url || "/";

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

console.log(`✅ Service Worker Initialized - Version: ${SW_VERSION}`);
