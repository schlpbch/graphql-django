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
  links {
    id
    username
    password
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
