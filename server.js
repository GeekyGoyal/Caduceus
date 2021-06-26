/**
 * @fileoverview Caduceus server
 */

 const port = 5000;
 const express = require("express");
 const app = express();
 const http = require("http");
 const server = http.createServer(app);
 const io = require("socket.io")(server);
 var currentPatientId = 0;
 var currentDoctorId = 0;
 
 server.listen(port);
 
 app.use(express.static(__dirname));
 
 app.get('/', function(req, res){
     res.sendFile(__dirname+"/index.html");
 });
 console.log("Node server started on port " + port);
 
 io.sockets.on("connection", (socket) => {
     console.log("user connected");
     socket.on("chat message", (msg) => {
         let content = msg.split("~~~");
         let roomNumber = content[0];
         let doctor = content[1];
         let message = content[2];
         let sender = "patient";
         if (doctor == "true") {
             sender = "doctor";
         }
         io.to(`room${roomNumber}`).emit("chat message", `${sender}: ${message}`);
     });
     socket.on("disconnect", () => {
         console.log("user disconnected");
     });
     socket.on("person", (person) => {
         if (person === "doctor") {
             socket.join(`room${currentDoctorId}`);
             io.to(`room${currentDoctorId}`).emit("number", currentDoctorId);
             currentDoctorId++;
         } else if (person === "patient") {
            socket.join(`room${currentPatientId}`);
            io.to(`room${currentDoctorId}`).emit("number", currentPatientId);
            currentPatientId++;
        }
     });
 });