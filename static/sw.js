

var cacheName = 'cozmato-v1';
const cacheAssets = [
    '/static/offline.png',
    '/static/offline.html'
];

// Call install Event
self.addEventListener('install', e => {
    // Wait until promise is finished
    e.waitUntil(
        caches
        .open(cacheName)
        .then(cache => {
           
            cache.addAll(cacheAssets);
            })
            .then(() => self.skipWaiting())
    );
})



// Call Activate Event
self.addEventListener('activate', e => {

    e.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(
                    cache => {
                        if (cache !== cacheName) {
                            return caches.delete(cache);
                        }
                    }
                )
            )
        })
    );
})

self.addEventListener("fetch", e => {
    e.respondWith(fetch(e.request).catch(() => caches.match(cacheAssets)))
});





