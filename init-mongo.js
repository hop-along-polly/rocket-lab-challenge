db = db.getSiblingDB('rocket-lab')
db.createCollection('nodes')
// TODO I can probably remove this since I can use the exists query.
// I kinda like it though b/c I could add a unique index to this and ensure
// the nodes collection then won't have many nodes with the same root node.
db.getCollection('root_nodes').insertMany([
  {
    "name": "Rocket"
  }
])
db.getCollection('nodes').insertMany([
  {
    "Rocket": {
      "Height": 18.000,
      "Mass": 12000.000,
      "Stage1": {
        "Engine1": {
          "Thrust": 9.493,
          "ISP": 12.156
        },
        "Engine2": {
          "Thrust": 9.413,
          "ISP": 11.632
        },
        "Engine3": {
          "Thrust": 9.899,
          "ISP": 12.551
        }
      },
      "Stage2": {
        "Engine1": {
          "Thrust": 1.622,
          "ISP": 15.110
        }
      }
    }
  }
]);
