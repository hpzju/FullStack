const MongoClient = require("mongodb").MongoClient;
const assert = require("assert");

(async function() {
  // Connection URL
  const url = "mongodb://localhost:27017/learn";
  // Database Name
  const dbName = "learn";
  const client = new MongoClient(url, { useNewUrlParser: true });

  try {
    // Use connect method to connect to the Server
    await client.connect();
    console.log("******Connected successfully to server");

    const db = client.db(dbName);

    // Get the collection
    const col = db.collection("errmsgs");

    // Get the cursor
    const cursor = col.find({}).limit(1);

    // Iterate over the cursor
    while (await cursor.hasNext()) {
      const doc = await cursor.next();
      console.log(doc);
    }
  } catch (err) {
    console.log(err.stack);
  }

  client.close();
  console.log("******Closed successfully to server");
})();
