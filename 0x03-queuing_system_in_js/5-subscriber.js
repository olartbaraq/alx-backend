import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const subscriber = client.duplicate();

const CHANNEL = 'holberton school channel'
subscriber.subscribe(CHANNEL, (message) => {
    if(CHANNEL) {
        console.log(message);
    }
    if(message === 'KILL_SERVER') {
        subscriber.unsubscribe('holberton school channel')
        subscriber.quit();
    }
    
});
