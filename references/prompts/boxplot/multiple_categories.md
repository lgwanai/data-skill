## 图表类型：多系列盒须图 (Multiple Categories)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// Generate data.
function makeData() {
  let data = [];
  for (let i = 0; i < 18; i++) {
    let cate = [];
    for (let j = 0; j < 100; j++) {
      cate.push(Math.random() * 200);
    }
    data.push(cate);
  }
  return data;
}
const data0 = makeData();
const data1 = makeData();
const data2 = makeData();
option = {
  title: {
    text: 'Multiple Categories',
    left: 'center'
  },
  dataset: [
    {
      source: data0
    },
    {
      source: data1
    },
    {
      source: data2
    },
    {
      fromDatasetIndex: 0,
      transform: { type: 'boxplot' }
    },
    {
      fromDatasetIndex: 1,
      transform: { type: 'boxplot' }
    },
    {
      fromDatasetIndex: 2,
      transform: { type: 'boxplot' }
    }
  ],
  legend: {
    top: '10%'
  },
  tooltip: {
    trigger: 'item',
    axisPointer: {
      type: 'shadow'
    }
  },
  grid: {
    left: '10%',
    top: '20%',
    right: '10%',
    bottom: '15%'
  },
  xAxis: {
    type: 'category',
    boundaryGap: true,
    nameGap: 30,
    splitArea: {
      show: true
    },
    splitLine: {
      show: false
    }
  },
  yAxis: {
    type: 'value',
    name: 'Value',
    min: -400,
    max: 600,
    splitArea: {
      show: false
    }
  },
  dataZoom: [
    {
      type: 'inside',
      start: 0,
      end: 20
    },
    {
      show: true,
      type: 'slider',
      top: '90%',
      xAxisIndex: [0],
      start: 0,
      end: 20
    }
  ],
  series: [
    {
      name: 'category0',
      type: 'boxplot',
      datasetIndex: 3
    },
    {
      name: 'category1',
      type: 'boxplot',
      datasetIndex: 4
    },
    {
      name: 'category2',
      type: 'boxplot',
      datasetIndex: 5
    }
  ]
};
```

