# GraphQL commands

## Query

Query links

```graphql
query {
  links {
    id
    description
    url
  }
}
```

Query Users

```graphql
query {
  users {
    id
    username
    password
  }
}
```

Query Votes

```graphql
query {
  votes {
    id
    user {
      id
      username
    }
    link {
      id
      url
    }
  }
}
```

## Mutate

Create link:

```graphql
mutation {
  createLink(
    url: "https://github.com",
    description: "Where the world builds software"
  ) {
    id
    description
    url
  }
}
```

```graphql
mutation {
  createLink(
    url: "https://github.com/schlpbch",
    description: "Schlpbch's GitHub"
  ) {
    id
    description
    url
    postedBy {
      id
      username
      email
    }
  }
}
```

Create user:

```graphql
mutation {
  createUser(
    username: "schlpbch",
    email: "schlpbch@gmail.com",
    password: "424242"
  ) {
    user {
      id
      username
      email
    }
  }
}
```

Create Vote

```graphql
mutation {
  createVote(linkId: 1) {
    user {
      id
      username
      email
    }
    link {
      id
      description
      url
    }
  } 
}
```
