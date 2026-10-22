export const onRequest = () => new Response('pong ' + new Date().toISOString(), { headers: { 'content-type': 'text/plain', 'cache-control': 'no-store' } });
