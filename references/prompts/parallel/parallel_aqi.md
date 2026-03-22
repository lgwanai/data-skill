## 图表类型：AQI 分布（平行坐标） (Parallel Aqi)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// Schema:
// date,AQIindex,PM2.5,PM10,CO,NO2,SO2
const dataBJ = [ /* 请使用用户的真实数据数组替换此处 */ ];
var dataGZ = [ /* 请使用用户的真实数据数组替换此处 */ ];
var dataSH = [ /* 请使用用户的真实数据数组替换此处 */ ];
var schema = [
  { name: 'date', index: 0, text: '日期' },
  { name: 'AQIindex', index: 1, text: 'AQI' },
  { name: 'PM25', index: 2, text: 'PM2.5' },
  { name: 'PM10', index: 3, text: 'PM10' },
  { name: 'CO', index: 4, text: ' CO' },
  { name: 'NO2', index: 5, text: 'NO2' },
  { name: 'SO2', index: 6, text: 'SO2' },
  { name: '等级', index: 7, text: '等级' }
];
var lineStyle = {
  width: 1,
  opacity: 0.5
};
option = {
  backgroundColor: '#333',
  legend: {
    bottom: 30,
    data: ['Beijing', 'Shanghai', 'Guangzhou'],
    itemGap: 20,
    textStyle: {
      color: '#fff',
      fontSize: 14
    }
  },
  tooltip: {
    padding: 10,
    backgroundColor: '#222',
    borderColor: '#777',
    borderWidth: 1
  },
  parallelAxis: [
    {
      dim: 0,
      name: schema[0].text,
      inverse: true,
      max: 31,
      nameLocation: 'start'
    },
    { dim: 1, name: schema[1].text },
    { dim: 2, name: schema[2].text },
    { dim: 3, name: schema[3].text },
    { dim: 4, name: schema[4].text },
    { dim: 5, name: schema[5].text },
    { dim: 6, name: schema[6].text },
    {
      dim: 7,
      name: schema[7].text,
      type: 'category',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  ],
  visualMap: {
    show: true,
    min: 0,
    max: 150,
    dimension: 2,
    inRange: {
      color: ['#d94e5d', '#eac736', '#50a3ba'].reverse()
      // colorAlpha: [0, 1]
    }
  },
  parallel: {
    left: '5%',
    right: '18%',
    bottom: 100,
    parallelAxisDefault: {
      type: 'value',
      name: 'AQI指数',
      nameLocation: 'end',
      nameGap: 20,
      nameTextStyle: {
        color: '#fff',
        fontSize: 12
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
      }
    }
  },
  series: [
    {
      name: 'Beijing',
      type: 'parallel',
      lineStyle: lineStyle,
      data: dataBJ
    },
    {
      name: 'Shanghai',
      type: 'parallel',
      lineStyle: lineStyle,
      data: dataSH
    },
    {
      name: 'Guangzhou',
      type: 'parallel',
      lineStyle: lineStyle,
      data: dataGZ
    }
  ]
};
```

