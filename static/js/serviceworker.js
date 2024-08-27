/*
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return cache.addAll([
        '',
      ]);
    })
  );
});



*/

const cacheName = 'cozmato-v1';

// Call install event
self.addEventListener("install", (e) => {
console.log('Service worker installed')
});


// Call activate event
self.addEventListener("activate", (e) => {
    // Remove unwanted caches
    e.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cache) => {
                    if (cache !== cacheName) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});



self.addEventListener('fetch', (event) => {
    if (event.request.method !== 'GET') {
        return;
    }

event.respondWith(
    caches.match(event.request)
        .then((response) => {
            console.log(`[SW] Requesting ${event.request.url}.`)
            if (response) {
                console.log(`[SW] Served response to ${event.request.url} from the cache.`);
                return response;
            }

            return fetch(event.request)
                .then(res => {
                    return caches.open(dynamicCacheName)
                        .then(cache => {
                            cache.put(event.request.url, res.clone());
                            return res;
                        })
                })
                .catch(err => console.warn('Warning: app is offline', err));
        }),
);


/*


// Call activate event
self.addEventListener("activate", (e) => {
    // Remove unwanted caches
    e.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cache) => {
                    if (cache !== cacheName) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});




// Call fetch event
self.addEventListener("fetch", (e) => {
    e.respondWith(fetch(e.request)
    .then(res => {
        const resClone = res.clone();
        caches.open(cacheName).then(cache => {
            cache.put(e.request, resClone);
        });
    return res;
    })
    .catch(err => caches.match(e.request).then(res => res))
    );
});


self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        if (response) {
          return response;
        }
        var fetchRequest = event.request.clone();
        return fetch(fetchRequest).then(
          function(response) {
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            var responseToCache = response.clone();
            caches.open(cacheName)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });
            return response;
          }
        );
      })
    );
});


*/




