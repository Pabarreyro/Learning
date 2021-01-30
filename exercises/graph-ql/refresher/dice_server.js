const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
    type Query {
        quoteOfTheDay: String
        random: Float!
        rollThreeDice: [Int]
    }
`);

// The root provides a resolver function for each API endpoint
const root = {
    quoteOfTheDay: () => Math.random() < 0.5 ? 'Take it easy' : 'Salvation lies within',
    random: () => Math.random(),
    rollThreeDice: () => [1, 2, 3].map(() => 1 + Math.floor(Math.random() * 6))
};

// Start GraphQL server and begin listening
const app = express();

app.use('/graphql', graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true
}));

app.listen(4000);

console.log('Running Dice Roller at localhost:4000/graphql');