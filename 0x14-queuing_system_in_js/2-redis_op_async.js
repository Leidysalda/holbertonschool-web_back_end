import redis from 'redis';
const { promisify } = require("util");

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(SchoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const foundValue = await get Async(schoolName);
    console.log(foundValue);
}

(async function main() {
    await function displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}());
