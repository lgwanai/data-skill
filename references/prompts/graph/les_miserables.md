## 图表类型：悲惨世界人物关系图(环形布局) (Les Miserables)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/les-miserables.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：nodes, links, categories。数据截取示例：
{
  "nodes": [
    {
      "id": "0",
      "name": "Myriel",
      "symbolSize": 19.12381,
      "x": -266.82776,
      "y": 299.6904,
      "value": 28.685715,
      "category": 0
    },
    {
      "id": "1",
      "name": "Napoleon",
      "symbolSize": 2.6666666666666665,
      "x": -418.08344,
      "y": 446.8853,
      "value": 4,
      "category": 0
    },
    {
      "id": "2",
      "name": "MlleBaptistine",
      "symbolSize": 6.323809333333333,
      "x": -212.76357,
      "y": 245.2...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
myChart.showLoading();
$.getJSON(ROOT_PATH + '/data/asset/data/les-miserables.json', function (graph) {
  myChart.hideLoading();
  graph.nodes.forEach(function (node) {
    node.label = {
      show: node.symbolSize > 30
    };
  });
  option = {
    title: {
      text: 'Les Miserables',
      subtext: 'Circular layout',
      top: 'bottom',
      left: 'right'
    },
    tooltip: {},
    legend: [
      {
        data: graph.categories.map(function (a) {
          return a.name;
        })
      }
    ],
    animationDurationUpdate: 1500,
    animationEasingUpdate: 'quinticInOut',
    series: [
      {
        name: 'Les Miserables',
        type: 'graph',
        layout: 'circular',
        circular: {
          rotateLabel: true
        },
        data: graph.nodes,
        links: graph.links,
        categories: graph.categories,
        roam: true,
        label: {
          position: 'right',
          formatter: '{b}'
        },
        lineStyle: {
          color: 'source',
          curveness: 0.3
        }
      }
    ]
  };
  myChart.setOption(option);
});
```

