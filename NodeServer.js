var http = require("http");

http.createServer(function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});
   
   // Send the response body as "Hello World"
   response.end('Hello World\n');
}).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');




var fs = require("fs");
console.log('\nImporting the following map data\n');

fs.readFile('map0.txt', function (err, data) {
   if (err) return console.error(err);
   console.log(data.toString());
});