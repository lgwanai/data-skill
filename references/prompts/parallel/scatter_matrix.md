## 图表类型：散点矩阵和平行坐标 (Scatter Matrix)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// Schema:
// date,AQIindex,PM2.5,PM10,CO,NO2,SO2
const schema = [
  { name: 'AQIindex', index: 1, text: 'AQI' },
  { name: 'PM25', index: 2, text: 'PM 2.5' },
  { name: 'PM10', index: 3, text: 'PM 10' },
  { name: 'CO', index: 4, text: 'CO' },
  { name: 'NO2', index: 5, text: 'NO₂' },
  { name: 'SO2', index: 6, text: 'SO₂' },
  { name: '等级', index: 7, text: '等级' }
];
const rawData = [ /* 请使用用户的真实数据数组替换此处 */ ];
const CATEGORY_DIM_COUNT = 6;
const GAP = 2;
const BASE_LEFT = 5;
const BASE_TOP = 10;
// const GRID_WIDTH = 220;
// const GRID_HEIGHT = 220;
const GRID_WIDTH = (100 - BASE_LEFT - GAP) / CATEGORY_DIM_COUNT - GAP;
const GRID_HEIGHT = (100 - BASE_TOP - GAP) / CATEGORY_DIM_COUNT - GAP;
const CATEGORY_DIM = 7;
const SYMBOL_SIZE = 4;
function retrieveScatterData(data, dimX, dimY) {
  let result = [];
  for (let i = 0; i < data.length; i++) {
    let item = [data[i][dimX], data[i][dimY]];
    item[CATEGORY_DIM] = data[i][CATEGORY_DIM];
    result.push(item);
  }
  return result;
}
function generateGrids() {
  let index = 0;
  const grid = [];
  const xAxis = [];
  const yAxis = [];
  const series = [];
  for (let i = 0; i < CATEGORY_DIM_COUNT; i++) {
    for (let j = 0; j < CATEGORY_DIM_COUNT; j++) {
      if (CATEGORY_DIM_COUNT - i + j >= CATEGORY_DIM_COUNT) {
        continue;
      }
      grid.push({
        left: BASE_LEFT + i * (GRID_WIDTH + GAP) + '%',
        top: BASE_TOP + j * (GRID_HEIGHT + GAP) + '%',
        width: GRID_WIDTH + '%',
        height: GRID_HEIGHT + '%'
      });
      xAxis.push({
        splitNumber: 3,
        position: 'top',
        axisLine: {
          show: j === 0,
          onZero: false
        },
        axisTick: {
          show: j === 0,
          inside: true
        },
        axisLabel: {
          show: j === 0
        },
        type: 'value',
        gridIndex: index,
        scale: true
      });
      yAxis.push({
        splitNumber: 3,
        position: 'right',
        axisLine: {
          show: i === CATEGORY_DIM_COUNT - 1,
          onZero: false
        },
        axisTick: {
          show: i === CATEGORY_DIM_COUNT - 1,
          inside: true
        },
        axisLabel: {
          show: i === CATEGORY_DIM_COUNT - 1
        },
        type: 'value',
        gridIndex: index,
        scale: true
      });
      series.push({
        type: 'scatter',
        symbolSize: SYMBOL_SIZE,
        xAxisIndex: index,
        yAxisIndex: index,
        data: retrieveScatterData(rawData, i, j)
      });
      index++;
    }
  }
  return {
    grid,
    xAxis,
    yAxis,
    series
  };
}
const gridOption = generateGrids();
option = {
  animation: false,
  brush: {
    brushLink: 'all',
    xAxisIndex: gridOption.xAxis.map(function (_, idx) {
      return idx;
    }),
    yAxisIndex: gridOption.yAxis.map(function (_, idx) {
      return idx;
    }),
    inBrush: {
      opacity: 1
    }
  },
  visualMap: {
    type: 'piecewise',
    categories: ['北京', '上海', '广州'],
    dimension: CATEGORY_DIM,
    orient: 'horizontal',
    top: 0,
    left: 'center',
    inRange: {
      color: ['#51689b', '#ce5c5c', '#fbc357']
    },
    outOfRange: {
      color: '#ddd'
    },
    seriesIndex: gridOption.series.map(function (_, idx) {
      return idx;
    })
  },
  tooltip: {
    trigger: 'item'
  },
  parallelAxis: [
    { dim: 0, name: schema[0].text },
    { dim: 1, name: schema[1].text },
    { dim: 2, name: schema[2].text },
    { dim: 3, name: schema[3].text },
    { dim: 4, name: schema[4].text },
    { dim: 5, name: schema[5].text },
    {
      dim: 6,
      name: schema[6].text,
      type: 'category',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  ],
  parallel: {
    bottom: '5%',
    left: '2%',
    height: '30%',
    width: '55%',
    parallelAxisDefault: {
      type: 'value',
      name: 'AQI指数',
      nameLocation: 'end',
      nameGap: 20,
      splitNumber: 3,
      nameTextStyle: {
        fontSize: 14
      },
      axisLine: {
        lineStyle: {
          color: '#555'
        }
      },
      axisTick: {
        lineStyle: {
          color: '#555'
        }
      },
      splitLine: {
        show: false
      },
      axisLabel: {
        color: '#555'
      }
    }
  },
  xAxis: gridOption.xAxis,
  yAxis: gridOption.yAxis,
  grid: gridOption.grid,
  series: [
    {
      name: 'parallel',
      type: 'parallel',
      smooth: true,
      lineStyle: {
        width: 1,
        opacity: 0.3
      },
      data: rawData
    },
    ...gridOption.series
  ]
};
```

