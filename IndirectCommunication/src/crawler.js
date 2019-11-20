const amqp = require("amqplib/callback_api");
const tweets = require("tweets");

const stream = new tweets({
  consumer_key: "934ny4ZHoJPmJqS8SDYxy2gTF",
  consumer_secret: "EYc4BJNFi0fUZc165gmigrVRQ7mSFzwzSUdResHltgHWSczfdO",
  access_token: "1711318230-sd9yp8yRUYTIUkthRnYmf6tbmlpR0WA6FBsadWo",
  access_token_secret: "3C1JlotF1akg3L9eU2x2BT9O1LqO7o9mEGq4KZphHIvRZ"
});

async function sendTweetMessageQueue(tweet, channel) {
  // Cada novo tweet que chega, é enviado para a fila que será consumida pelo classificador
  const queue = "tweets";
  channel.sendToQueue(queue, Buffer.from(tweet), { persistent: true });

  console.log("Tweet enviado para a fila de mensagens: %s", tweet);
}

amqp.connect("amqp://localhost", function(error0, connection) {
  if (error0) {
    throw error0;
  }

  connection.createChannel(function(error1, channel) {
    if (error1) {
      throw error1;
    }

    const queue = "tweets";
    channel.assertQueue(queue, { durable: true });

    stream.filter({ track: ["basquete", "volei"] });

    stream.on("tweet", function(t) {
      sendTweetMessageQueue(t.text, channel);
    });
  });
});
