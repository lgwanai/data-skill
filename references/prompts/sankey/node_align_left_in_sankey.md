## 图表类型：桑基图左对齐布局 (Node Align Left in Sankey)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/energy.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：nodes, links。数据截取示例：
{
  "nodes": [
    {
      "name": "Agricultural 'waste'"
    },
    {
      "name": "Bio-conversion"
    },
    {
      "name": "Liquid"
    },
    {
      "name": "Losses"
    },
    {
      "name": "Solid"
    },
    {
      "name": "Gas"
    },
    {
      "name": "Biofuel imports"
    },
    {
      "name": "Biomass imports"
    },
    {
      "name": "Coal imports"
    },
    {
      "name": "Coal"
    },
    {
      "name": "Coal reserves"
    },
    {
      "name": "District heating"
   ...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
myChart.showLoading();
$.get(ROOT_PATH + '/data/asset/data/energy.json', function (data) {
  myChart.hideLoading();
  myChart.setOption(
    (option = {
      title: {
        text: 'Node Align Left'
      },
      tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove'
      },
      series: [
        {
          type: 'sankey',
          emphasis: {
            focus: 'adjacency'
          },
          nodeAlign: 'left',
          data: data.nodes,
          links: data.links,
          lineStyle: {
            color: 'source',
            curveness: 0.5
          }
        }
      ]
    })
  );
});
```

