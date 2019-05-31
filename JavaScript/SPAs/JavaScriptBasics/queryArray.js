const arrTree = [
  {
    header: "L1",
    data: "L1:this is the root",
    nodes: [
      {
        header: "L2",
        data: "L2: this is the node1",
        nodes: [
          {
            header: "L3",
            data: "L3: this is the node1",
            nodes: []
          }
        ]
      },
      {
        header: "L2",
        data: "L2: this is the node2",
        nodes: [
          {},
          {},
          {
            header: "L3",
            data: "L3: this is the node3",
            nodes: []
          }
        ]
      },
      {
        header: "L2",
        data: "L2: this is the node3",
        nodes: []
      }
    ]
  },
  {
    header: "L1",
    data: "L1: this is the root2",
    nodes: []
  },
  {
    data: "this is the root3"
  }
];

// console.log(arrTree);
// console.log([{}, {}, {}] ? true : false);

const querryArr = (arr, property) => {
  return arr.filter(e => (e[property] ? true : false)).map(e => e[property]);
};

const querryNestedArr = (arr, property) =>
  arr
    .filter(e => (e[property] || e.nodes ? true : false))
    .reduce((accumer, e2) => {
      const nodesArr = e2.nodes.filter(e3 =>
        e3[property] || e3.nodes ? true : false
      );
      nodesArr.length > 0
        ? accumer.push(querryNestedArr(nodesArr, property))
        : accumer.push(e2[property]);

      return accumer;
    }, []);

// console.log(querryArr(arrTree, "header"));
// console.log(querryArr(arrTree, "data"));
// console.log(querryArr(arrTree, "nodes"));
// const querryHeader = arr => querryArr(arr, "header");
// const querryData = arr => querryArr(arr, "data");
// const querryNodes = arr => querryArr(arr, "nodes");

// console.log(querryHeader(arrTree));
// console.log(querryData(arrTree));
// console.log(querryNodes(arrTree));

const querryHeader = arr => querryNestedArr(arr, "header");
const querryData = arr => querryNestedArr(arr, "data");
const querryNodes = arr => querryArr(arr, "nodes");

console.log(querryData(arrTree));
