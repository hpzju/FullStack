const MongoClient = require("mongodb").MongoClient;
const assert = require("assert");

// Connection URL
const url = "mongodb://localhost:27017";

// Database Name
const dbName = "learn";

// Create a new MongoClient
const client = new MongoClient(url, { useNewUrlParser: true });

// Use connect method to connect to the Server
client.connect(function(err) {
  assert.equal(null, err);
  console.log("*******Connected successfully to server");

  const db_learn = client.db(dbName);

  db_learn.collection("errmsgs").findOne({}, function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records");
    console.log(docs);
    client.close();
    console.log("*******Connection terminated correctly.");
  });
});
