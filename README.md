# GraphQL commands

## Query

```graphql
query {
  links {
    id
    description
    url
  }
}
```

## Mutate

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
