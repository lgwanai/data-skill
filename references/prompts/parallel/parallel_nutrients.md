## 图表类型：营养结构（平行坐标） (Parallel Nutrients)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/nutrients.json]**:
```json
数据是一个数组 (Array)，共 7637 项。单项结构示例：
[
  [
    "Beverage, instant breakfast powder, chocolate, not reconstituted",
    "Dairy and Egg Products",
    19.9,
    0.285,
    0.385,
    0.4,
    0.07690000000000001,
    0.947,
    66.2,
    65.8,
    1.4,
    7.4,
    357,
    0.56,
    0.314,
    0.278,
    27481
  ],
  [
    "Beverage, instant breakfast powder, chocolate, sugar-free, not reconstituted",
    "Dairy and Egg Products",
    35.8,
    0.5,
    0.717,
    2,
    0.138,
    1.705,
    41,
    39,
    5.1,
    7.4,
    358,
    2.162,
    1.189,
    1.027,
    27482
  ]
]
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const indices = {
  name: 0,
  group: 1,
  id: 16
};
const schema = [
  { name: 'name', index: 0 },
  { name: 'group', index: 1 },
  { name: 'protein', index: 2 },
  { name: 'calcium', index: 3 },
  { name: 'sodium', index: 4 },
  { name: 'fiber', index: 5 },
  { name: 'vitaminc', index: 6 },
  { name: 'potassium', index: 7 },
  { name: 'carbohydrate', index: 8 },
  { name: 'sugars', index: 9 },
  { name: 'fat', index: 10 },
  { name: 'water', index: 11 },
  { name: 'calories', index: 12 },
  { name: 'saturated', index: 13 },
  { name: 'monounsat', index: 14 },
  { name: 'polyunsat', index: 15 },
  { name: 'id', index: 16 }
];
const groupCategories = [];
const groupColors = [];
$.get(ROOT_PATH + '/data/asset/data/nutrients.json', function (data) {
  normalizeData(data);
  myChart.setOption((option = getOption(data)));
});
function normalizeData(originData) {
  const groupMap = {};
  originData.forEach(function (row) {
    const groupName = row[indices.group];
    if (!groupMap.hasOwnProperty(groupName)) {
      groupMap[groupName] = 1;
    }
  });
  originData.forEach(function (row) {
    row.forEach(function (item, index) {
      if (
        index !== indices.name &&
        index !== indices.group &&
        index !== indices.id
      ) {
        // Convert null to zero, as all of them under unit "g".
        row[index] = parseFloat(item) || 0;
      }
    });
  });
  for (const groupName in groupMap) {
    if (groupMap.hasOwnProperty(groupName)) {
      groupCategories.push(groupName);
    }
  }
  const hStep = Math.round(300 / (groupCategories.length - 1));
  for (var i = 0; i < groupCategories.length; i++) {
    groupColors.push(echarts.color.modifyHSL('#5A94DF', hStep * i));
  }
}
function getOption(data) {
  const lineStyle = {
    width: 0.5,
    opacity: 0.05
  };
  return {
    backgroundColor: '#333',
    tooltip: {
      padding: 10,
      backgroundColor: '#222',
      borderColor: '#777',
      borderWidth: 1
    },
    title: [
      {
        text: 'Groups',
        top: 0,
        left: 0,
        textStyle: {
          color: '#fff'
        }
      }
    ],
    visualMap: {
      show: true,
      type: 'piecewise',
      categories: groupCategories,
      dimension: indices.group,
      inRange: {
        color: groupColors //['#d94e5d','#eac736','#50a3ba']
      },
      outOfRange: {
        color: ['#ccc'] //['#d94e5d','#eac736','#50a3ba']
      },
      top: 20,
      textStyle: {
        color: '#fff'
      },
      realtime: false
    },
    parallelAxis: [
      { dim: 16, name: schema[16].name, scale: true, nameLocation: 'end' },
      { dim: 2, name: schema[2].name, nameLocation: 'end' },
      { dim: 4, name: schema[4].name, nameLocation: 'end' },
      { dim: 3, name: schema[3].name, nameLocation: 'end' },
      { dim: 5, name: schema[5].name, nameLocation: 'end' },
      { dim: 6, name: schema[6].name, nameLocation: 'end' },
      { dim: 7, name: schema[7].name, nameLocation: 'end' },
      { dim: 8, name: schema[8].name, nameLocation: 'end' },
      { dim: 9, name: schema[9].name, nameLocation: 'end' },
      { dim: 10, name: schema[10].name, nameLocation: 'end' },
      { dim: 11, name: schema[11].name, nameLocation: 'end' },
      { dim: 12, name: schema[12].name, nameLocation: 'end' },
      { dim: 13, name: schema[13].name, nameLocation: 'end' },
      { dim: 14, name: schema[14].name, nameLocation: 'end' },
      { dim: 15, name: schema[15].name, nameLocation: 'end' }
    ],
    parallel: {
      left: 280,
      top: 20,
      // top: 150,
      // height: 300,
      width: 400,
      layout: 'vertical',
      parallelAxisDefault: {
        type: 'value',
        name: 'nutrients',
        nameLocation: 'end',
        nameGap: 20,
        nameTextStyle: {
          color: '#fff',
          fontSize: 14
        },
        axisLine: {
          lineStyle: {
            color: '#aaa'
          }
        },
        axisTick: {
          lineStyle: {
            color: '#777'
          }
        },
        splitLine: {
          show: false
        },
        axisLabel: {
          color: '#fff'
        },
        realtime: false
      }
    },
    animation: false,
    series: [
      {
        name: 'nutrients',
        type: 'parallel',
        lineStyle: lineStyle,
        inactiveOpacity: 0,
        activeOpacity: 0.01,
        progressive: 500,
        smooth: true,
        data: data
      }
    ]
  };
}
```

