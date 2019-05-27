require('dotenv').config()

var Snoowrap = require('snoowrap')
var Snoostorm = require('snoostorm')

var r = new Snoowrap({
    userAgent: 'reddit-bot-example-node',
    clientId: process.env.CLIENT_ID,
    clientSecret: process.env.CLIENT_SECRET,
    username: process.env.REDDIT_USER,
    password: process.env.REDDIT_PASS
})

var client = new Snoostorm(r)

// Configure options for stream: subreddit & results per query
var streamOpts = {
    subreddit: 'NoahBM',
    results: 25
}

// Create a Snoostorm CommentStream with the specified options
var comments = client.CommentStream(streamOpts)

// On comment, perform whatever logic you want to do
/*comments.on('comment', (comment) => {
    console.log(comment);
});*/

if (comment.body === 'test') {
    comment.reply('test success')
}
