## 图表类型：营养分布散点图 (Scatter Nutrients)

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
const fieldIndices = schema.reduce(function (obj, item) {
  obj[item.name] = item.index;
  return obj;
}, {});
const groupCategories = [];
const groupColors = [];
let data;
// zlevel 为 1 的层开启尾迹特效
myChart.getZr().configLayer(1, {
  motionBlur: true
});
$.get(ROOT_PATH + '/data/asset/data/nutrients.json', function (originData) {
  data = normalizeData(originData).slice(0, 1000);
  myChart.setOption((option = getOption(data)));
});
function normalizeData(originData) {
  let groupMap = {};
  originData.forEach(function (row) {
    let groupName = row[indices.group];
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
  for (let groupName in groupMap) {
    if (groupMap.hasOwnProperty(groupName)) {
      groupCategories.push(groupName);
    }
  }
  let hStep = Math.round(300 / (groupCategories.length - 1));
  for (let i = 0; i < groupCategories.length; i++) {
    groupColors.push(echarts.color.modifyHSL('#5A94DF', hStep * i));
  }
  return originData;
}
function getOption(data) {
  return {
    xAxis: {
      name: 'protein',
      splitLine: { show: false }
    },
    yAxis: {
      name: 'calcium',
      splitLine: { show: false }
    },
    visualMap: [
      {
        show: false,
        type: 'piecewise',
        categories: groupCategories,
        dimension: 2,
        inRange: {
          color: groupColors
        },
        outOfRange: {
          color: ['#ccc']
        },
        top: 20,
        textStyle: {
          color: '#fff'
        },
        realtime: false
      },
      {
        show: false,
        dimension: 3,
        max: 100,
        inRange: {
          colorLightness: [0.15, 0.6]
        }
      }
    ],
    series: [
      {
        zlevel: 1,
        name: 'nutrients',
        type: 'scatter',
        data: data.map(function (item, idx) {
          return [item[2], item[3], item[1], idx];
        }),
        animationThreshold: 5000,
        progressiveThreshold: 5000
      }
    ],
    animationEasingUpdate: 'cubicInOut',
    animationDurationUpdate: 2000
  };
}
let fieldNames = schema
  .map(function (item) {
    return item.name;
  })
  .slice(2);
app.config = {
  xAxis: 'protein',
  yAxis: 'calcium',
  onChange: function () {
    if (data) {
      myChart.setOption({
        xAxis: {
          name: app.config.xAxis
        },
        yAxis: {
          name: app.config.yAxis
        },
        series: {
          data: data.map(function (item, idx) {
            return [
              item[fieldIndices[app.config.xAxis]],
              item[fieldIndices[app.config.yAxis]],
              item[1],
              idx
            ];
          })
        }
      });
    }
  }
};
app.configParameters = {
  xAxis: {
    options: fieldNames
  },
  yAxis: {
    options: fieldNames
  }
};
```

