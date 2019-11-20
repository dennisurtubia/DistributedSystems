const amqp = require("amqplib/callback_api");

amqp.connect("amqp://localhost", function(error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function(error1, channel) {
    if (error1) {
      throw error1;
    }
    const exchange = "tweets";
    const key = "football.tweets";
    const msg = messageQueue.pop() || "nao recebeu";
    console.log(msg);

    channel.assertExchange(exchange, "topic", {
      durable: false
    });
    if (messageQueue.length > 0) {
      channel.publish(exchange, key, Buffer.from(msg));
      console.log("Mensagem publicada: " + msg);
    }
  });

  setTimeout(function() {
    connection.close();
    process.exit(0);
  }, 500);
});

module.exports = { addTweetToQueue };


// function createConnection() {
//   amqp.connect('amqp://localhost', function(error0, connection) {
//   if (error0) {
//     throw error0;
//   }
//   channel = connection.createChannel(function(error1, channel) {
//     if (error1) {
//       throw error1;
//     }
    
//     return channel;
//   });

//     setTimeout(function() { 
//       connection.close(); 
//       process.exit(0); 
//     }, 500);
//   });

//   return channel;
// }

// function publishFootballMessage(channel, message) {
//   const exchange = 'footballTweets';
//   const key = 'football.tweets';

//   channel.assertExchange(exchange, 'topic', {
//     durable: false
//   });

//   channel.publish(exchange, key, Buffer.from(message));
//   console.log('Mensagem publicada: ' + message);
// }

// function publishVolleyMessage(channel, message) {
//   const exchange = 'volleyTweets';
//   const key = 'volley.tweets';

//   channel.assertExchange(exchange, 'topic', {
//     durable: false
//   });

//   channel.publish(exchange, key, Buffer.from(message));
//   console.log('Mensagem publicada: ' + message);
// }

// function classifyAndPublish(msg) {
//   const footballRegex = /futebol/gmi;
//   const volleyRegex = /volei/gmi;

//   if (footballRegex.test(msg)) publishFootballMessage(msg);
//   if (volleyRegex.test(msg)) publishVolleyMessage(msg);
// }

// createConnection();
// streamInit();