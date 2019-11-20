const amqp = require("amqplib/callback_api");

async function publishFootballMessage(channel, message) {
  const exchange = 'tweets';
  const key = 'football.tweets';

  channel.publish(exchange, key, Buffer.from(message));
  console.log('Mensagem publicada: ' + message);
}

async function publishVolleyMessage(message, channel) {
  const exchange = 'tweets';
  const key = 'volley.tweets';

  channel.publish(exchange, key, Buffer.from(message));
  console.log('Mensagem publicada: ' + message);
}

async function classifyAndPublish(msg, channel) {
  const footballRegex = /futebol/gmi;
  const volleyRegex = /volei/gmi;

  if (footballRegex.test(msg)) publishFootballMessage(msg, channel);
  if (volleyRegex.test(msg)) publishVolleyMessage(msg, channel);
}

amqp.connect("amqp://localhost", function(error0, connection) {
  if (error0) {
    throw error0;
  }

  connection.createChannel(function(error1, channel) {
    if (error1) {
      throw error1;
    }

    const exchange = "tweets";
    const queue = "tweets";

    channel.assertExchange(exchange, "topic", {
      durable: false
    });

    console.log("Waiting for tweets. To exit press CTRL+C");

    channel.consume(queue, function(tweet) {
      console.log("Tweet recieved: %s", tweet.content.toString());
      classifyAndPublish(tweet.content.toString(), channel);
    }, {
      noAck: true,
    });
  });
});
