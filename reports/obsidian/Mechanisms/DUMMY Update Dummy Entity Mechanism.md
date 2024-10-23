## Description

A mechanism which appends the word just added and also increments the total length
## Called By
1. [[DUMMY Letter Count Policy]]
2. [[DUMMY Letter Count Policy]]
## Domain Spaces
1. [[DUMMY String Length Space]]
## Constraints
## Logic
1. Append the string from DOMAIN[0] to the Words state variable for DUMMY entity
    2. Increment the Total Length state variable by the length from DOMAIN[0]

## Updates

1. [[DUMMY Entity]].[[DUMMY State-Words|Words]]
2. [[DUMMY Entity]].[[DUMMY State-Total Length|Total Length]]
