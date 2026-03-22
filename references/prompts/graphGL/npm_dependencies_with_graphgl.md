## 图表类型：1w 节点 2w7 边的 NPM 依赖图 (NPM Dependencies with graphGL)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data-gl/asset/data/npmdep.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：nodes, edges, dependentsCount。数据截取示例：
{
  "nodes": [
    "mocha",
    "chai",
    "lodash",
    "grunt",
    "eslint",
    "gulp",
    "babel-preset-es2015",
    "request",
    "async",
    "istanbul",
    "should",
    "express",
    "babel-core",
    "sinon",
    "babel-cli",
    "tape",
    "grunt-contrib-jshint",
    "underscore",
    "coffee-script",
    "webpack",
    "babel-eslint",
    "browserify",
    "chalk",
    "commander",
    "react",
    "babel-loader",
    "coveralls",
    "rimraf",
    "jshint",
    "debug",
    "b...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getJSON(ROOT_PATH + '/data-gl/asset/data/npmdep.json', function (data) {
  var nodes = data.nodes.map(function (nodeName, idx) {
    return {
      name: nodeName,
      value: data.dependentsCount[idx]
    };
  });
  var edges = [];
  for (var i = 0; i < data.edges.length; ) {
    var s = data.edges[i++];
    var t = data.edges[i++];
    edges.push({
      source: s,
      target: t
    });
  }
  nodes.forEach(function (node) {
    // if (node.value > 100) {
    node.emphasis = {
      label: {
        show: true
      }
    };
    // }
    if (node.value > 5000) {
      node.label = {
        show: true
      };
    }
  });
  myChart.setOption({
    backgroundColor: '#000',
    series: [
      {
        color: [ /* 请使用用户的真实数据数组替换此处 */ ],
        type: 'graphGL',
        nodes: nodes,
        edges: edges,
        modularity: {
          resolution: 2,
          sort: true
        },
        lineStyle: {
          color: 'rgba(255,255,255,1)',
          opacity: 0.05
        },
        itemStyle: {
          opacity: 1
          // borderColor: '#fff',
          // borderWidth: 1
        },
        focusNodeAdjacency: false,
        focusNodeAdjacencyOn: 'click',
        symbolSize: function (value) {
          return Math.sqrt(value / 10);
        },
        label: {
          color: '#fff'
        },
        emphasis: {
          label: {
            show: false
          },
          lineStyle: {
            opacity: 0.5,
            width: 4
          }
        },
        forceAtlas2: {
          steps: 5,
          stopThreshold: 20,
          jitterTolerence: 10,
          edgeWeight: [0.2, 1],
          gravity: 5,
          edgeWeightInfluence: 0
          // preventOverlap: true
        }
      }
    ]
  });
});
```

