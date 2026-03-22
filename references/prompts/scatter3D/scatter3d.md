## 图表类型：三维散点图 (Scatter3D)

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
var indices = {
  name: 0,
  group: 1,
  id: 16
};
var schema = [
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
var data;
var fieldIndices = schema.reduce(function (obj, item) {
  obj[item.name] = item.index;
  return obj;
}, {});
var groupCategories = [];
var groupColors = [];
var data;
var fieldNames = schema.map(function (item) {
  return item.name;
});
fieldNames = fieldNames.slice(2, fieldNames.length - 2);
function getMaxOnExtent(data) {
  var colorMax = -Infinity;
  var symbolSizeMax = -Infinity;
  for (var i = 0; i < data.length; i++) {
    var item = data[i];
    var colorVal = item[fieldIndices[config.color]];
    var symbolSizeVal = item[fieldIndices[config.symbolSize]];
    colorMax = Math.max(colorVal, colorMax);
    symbolSizeMax = Math.max(symbolSizeVal, symbolSizeMax);
  }
  return {
    color: colorMax,
    symbolSize: symbolSizeMax
  };
}
var config = (app.config = {
  xAxis3D: 'protein',
  yAxis3D: 'fiber',
  zAxis3D: 'sodium',
  color: 'fiber',
  symbolSize: 'vitaminc',
  onChange: function () {
    var max = getMaxOnExtent(data);
    if (data) {
      myChart.setOption({
        visualMap: [
          {
            max: max.color / 2
          },
          {
            max: max.symbolSize / 2
          }
        ],
        xAxis3D: {
          name: config.xAxis3D
        },
        yAxis3D: {
          name: config.yAxis3D
        },
        zAxis3D: {
          name: config.zAxis3D
        },
        series: {
          dimensions: [
            config.xAxis3D,
            config.yAxis3D,
            config.yAxis3D,
            config.color,
            config.symbolSiz
          ],
          data: data.map(function (item, idx) {
            return [
              item[fieldIndices[config.xAxis3D]],
              item[fieldIndices[config.yAxis3D]],
              item[fieldIndices[config.zAxis3D]],
              item[fieldIndices[config.color]],
              item[fieldIndices[config.symbolSize]],
              idx
            ];
          })
        }
      });
    }
  }
});
app.configParameters = {};
['xAxis3D', 'yAxis3D', 'zAxis3D', 'color', 'symbolSize'].forEach(function (
  fieldName
) {
  app.configParameters[fieldName] = {
    options: fieldNames
  };
});
$.getJSON(ROOT_PATH + '/data/asset/data/nutrients.json', function (_data) {
  data = _data;
  var max = getMaxOnExtent(data);
  myChart.setOption({
    tooltip: {},
    visualMap: [
      {
        top: 10,
        calculable: true,
        dimension: 3,
        max: max.color / 2,
        inRange: {
          color: [ /* 请使用用户的真实数据数组替换此处 */ ]
        },
        textStyle: {
          color: '#fff'
        }
      },
      {
        bottom: 10,
        calculable: true,
        dimension: 4,
        max: max.symbolSize / 2,
        inRange: {
          symbolSize: [10, 40]
        },
        textStyle: {
          color: '#fff'
        }
      }
    ],
    xAxis3D: {
      name: config.xAxis3D,
      type: 'value'
    },
    yAxis3D: {
      name: config.yAxis3D,
      type: 'value'
    },
    zAxis3D: {
      name: config.zAxis3D,
      type: 'value'
    },
    grid3D: {
      axisLine: {
        lineStyle: {
          color: '#fff'
        }
      },
      axisPointer: {
        lineStyle: {
          color: '#ffbd67'
        }
      },
      viewControl: {
        // autoRotate: true
        // projection: 'orthographic'
      }
    },
    series: [
      {
        type: 'scatter3D',
        dimensions: [
          config.xAxis3D,
          config.yAxis3D,
          config.yAxis3D,
          config.color,
          config.symbolSiz
        ],
        data: data.map(function (item, idx) {
          return [
            item[fieldIndices[config.xAxis3D]],
            item[fieldIndices[config.yAxis3D]],
            item[fieldIndices[config.zAxis3D]],
            item[fieldIndices[config.color]],
            item[fieldIndices[config.symbolSize]],
            idx
          ];
        }),
        symbolSize: 12,
        // symbol: 'triangle',
        itemStyle: {
          borderWidth: 1,
          borderColor: 'rgba(255,255,255,0.8)'
        },
        emphasis: {
          itemStyle: {
            color: '#fff'
          }
        }
      }
    ]
  });
});
```

