## 图表类型：流式渲染和视觉映射操作 (Visual interaction with stream)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/house-price-area2.json]**:
```json
数据是一个数组 (Array)，共 16174 项。单项结构示例：
[
  [
    18.78,
    22365
  ],
  [
    49.26,
    18271
  ]
]
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// Thanks to: 若怀冰
// http://gallery.echartsjs.com/explore.html?u=bd-16906679
// http://gallery.echartsjs.com/editor.html?c=xHJw-hVqjW
$.getJSON(
  ROOT_PATH + '/data/asset/data/house-price-area2.json',
  function (data) {
    var option = {
      title: {
        text: 'Dispersion of house price based on the area',
        left: 'center',
        top: 0
      },
      visualMap: {
        min: 15202,
        max: 159980,
        dimension: 1,
        orient: 'vertical',
        right: 10,
        top: 'center',
        text: ['HIGH', 'LOW'],
        calculable: true,
        inRange: {
          color: ['#f2c31a', '#24b7f2']
        }
      },
      tooltip: {
        trigger: 'item',
        axisPointer: {
          type: 'cross'
        }
      },
      xAxis: [
        {
          type: 'value'
        }
      ],
      yAxis: [
        {
          type: 'value'
        }
      ],
      series: [
        {
          name: 'price-area',
          type: 'scatter',
          symbolSize: 5,
          data: data
        }
      ]
    };
    myChart.setOption(option);
  }
);
```

