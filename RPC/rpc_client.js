const net = require('net');
const client = new net.Socket();

client.connect(65432, '127.0.0.1', () => {
    console.log('Connected to server');

    const request = {
        method: "nroot",
        params: [2, 16],
        id: 1
    };

    client.write(JSON.stringify(request));
});

client.on('data', (data) => {
    console.log('Received:', data.toString());
    client.destroy();
});

client.on('close', () => {
    console.log('Connection closed');
});

client.on('error', (err) => {
    console.error("Error:", err.message);
});
