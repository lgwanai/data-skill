## 图表类型：GraphGL - 大规模互联网图谱 (GraphGL - Large Internet)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data-gl/asset/data/internet.graph.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：nodes, edges。数据截取示例：
{
  "nodes": [
    [
      249,
      -33,
      4,
      4
    ],
    [
      251,
      -143,
      4,
      4
    ],
    [
      -715,
      234,
      4,
      0
    ],
    [
      -717,
      290,
      4,
      0
    ],
    [
      308,
      1190,
      4,
      13
    ],
    [
      -227,
      1474,
      4,
      13
    ],
    [
      143,
      502,
      4,
      15
    ],
    [
      738,
      -1719,
      4,
      5
    ],
    [
      820,
      -1902,
      4,
      5
    ],
    ...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getJSON(
  ROOT_PATH + '/data-gl/asset/data/internet.graph.json',
  function (graph) {
    var edges = graph.edges.map(function (edge) {
      return {
        source: edge[0],
        target: edge[1],
        value: 2
      };
    });
    var categories = [];
    var categoriesMap = {};
    var nodes = graph.nodes.map(function (node) {
      if (!categoriesMap[node[3]]) {
        categories.push({
          name: node[3]
        });
        categoriesMap[node[3]] = true;
      }
      return {
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        // x: node[0],
        // y: node[1],
        symbolSize: node[2],
        category: node[3],
        value: 1
      };
    });
    myChart.setOption({
      color: [ /* 请使用用户的真实数据数组替换此处 */ ],
      series: [
        {
          type: 'graphGL',
          nodes: nodes,
          edges: edges,
          categories: categories.sort(function (a, b) {
            return a.name - b.name;
          }),
          lineStyle: {
            color: 'rgba(255,255,255,0.2)'
          },
          itemStyle: {
            opacity: 1
          },
          forceAtlas2: {
            steps: 1,
            stopThreshold: 1,
            jitterTolerence: 10,
            edgeWeight: [0.2, 1],
            gravity: 0,
            edgeWeightInfluence: 1,
            scaling: 0.2
          }
        }
      ]
    });
  }
);
```

