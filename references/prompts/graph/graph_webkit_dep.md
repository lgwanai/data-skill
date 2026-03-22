## 图表类型：WebKit 模块关系依赖图 (Graph Webkit Dep)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/webkit-dep.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：type, categories, nodes, links。数据截取示例：
{
  "type": "force",
  "categories": [
    {
      "name": "HTMLElement",
      "keyword": {},
      "base": "HTMLElement"
    },
    {
      "name": "WebGL",
      "keyword": {},
      "base": "WebGLRenderingContext"
    },
    {
      "name": "SVG",
      "keyword": {},
      "base": "SVGElement"
    },
    {
      "name": "CSS",
      "keyword": {},
      "base": "CSSRule"
    },
    {
      "name": "Other",
      "keyword": {}
    }
  ],
  "nodes": [
    {
      "name": "AnalyserNode",
     ...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
myChart.showLoading();
myChart.showLoading();
$.get(ROOT_PATH + '/data/asset/data/webkit-dep.json', function (webkitDep) {
  myChart.hideLoading();
  option = {
    legend: {
      data: ['HTMLElement', 'WebGL', 'SVG', 'CSS', 'Other']
    },
    series: [
      {
        type: 'graph',
        layout: 'force',
        animation: false,
        roam: true,
        roamTrigger: 'global',
        scaleLimit: {
          max: 8,
          min: 0.5
        },
        label: {
          position: 'right',
          formatter: '{b}'
        },
        draggable: true,
        data: webkitDep.nodes.map(function (node, idx) {
          node.id = idx;
          return node;
        }),
        categories: webkitDep.categories,
        force: {
          edgeLength: 5,
          repulsion: 20,
          gravity: 0.2
        },
        edges: webkitDep.links
      }
    ],
    thumbnail: {
      width: '15%',
      height: '15%',
      windowStyle: {
        color: 'rgba(140, 212, 250, 0.5)',
        borderColor: 'rgba(30, 64, 175, 0.7)',
        opacity: 1
      }
    }
  };
  myChart.setOption(option);
});
```

