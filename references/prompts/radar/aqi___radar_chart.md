## 图表类型：AQI - 雷达图 (AQI - Radar Chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// Schema:
// date,AQIindex,PM2.5,PM10,CO,NO2,SO2
const dataBJ = [ /* 请使用用户的真实数据数组替换此处 */ ];
const dataGZ = [ /* 请使用用户的真实数据数组替换此处 */ ];
const dataSH = [ /* 请使用用户的真实数据数组替换此处 */ ];
const lineStyle = {
  width: 1,
  opacity: 0.5
};
option = {
  backgroundColor: '#161627',
  title: {
    text: 'AQI - Radar',
    left: 'center',
    textStyle: {
      color: '#eee'
    }
  },
  legend: {
    bottom: 5,
    data: ['Beijing', 'Shanghai', 'Guangzhou'],
    itemGap: 20,
    textStyle: {
      color: '#fff',
      fontSize: 14
    },
    selectedMode: 'single'
  },
  radar: {
    indicator: [
      { name: 'AQI', max: 300 },
      { name: 'PM2.5', max: 250 },
      { name: 'PM10', max: 300 },
      { name: 'CO', max: 5 },
      { name: 'NO2', max: 200 },
      { name: 'SO2', max: 100 }
    ],
    shape: 'circle',
    splitNumber: 5,
    axisName: {
      color: 'rgb(238, 197, 102)'
    },
    splitLine: {
      lineStyle: {
        color: [ /* 请使用用户的真实数据数组替换此处 */ ].reverse()
      }
    },
    splitArea: {
      show: false
    },
    axisLine: {
      lineStyle: {
        color: 'rgba(238, 197, 102, 0.5)'
      }
    }
  },
  series: [
    {
      name: 'Beijing',
      type: 'radar',
      lineStyle: lineStyle,
      data: dataBJ,
      symbol: 'none',
      itemStyle: {
        color: '#F9713C'
      },
      areaStyle: {
        opacity: 0.1
      }
    },
    {
      name: 'Shanghai',
      type: 'radar',
      lineStyle: lineStyle,
      data: dataSH,
      symbol: 'none',
      itemStyle: {
        color: '#B3E4A1'
      },
      areaStyle: {
        opacity: 0.05
      }
    },
    {
      name: 'Guangzhou',
      type: 'radar',
      lineStyle: lineStyle,
      data: dataGZ,
      symbol: 'none',
      itemStyle: {
        color: 'rgb(238, 197, 102)'
      },
      areaStyle: {
        opacity: 0.05
      }
    }
  ]
};
```

