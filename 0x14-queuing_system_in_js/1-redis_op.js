import redis from 'redis';
const client = redis.createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(SchoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(achoolName) {
    const foundValue = client.get(schoolName, redis.print);
    console.log(foundValue);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
