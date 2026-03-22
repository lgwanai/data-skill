## 图表类型：使用自定系列给散点图添加误差范围 (Error Scatter on Catesian)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// Prime Costs and Prices for ACME Fashion\nCollection "Spring-Summer, 2016"
// Data from https://playground.anychart.com/gallery/7.12.0/Error_Charts/Marker_Chart
// prettier-ignore
const dimensions = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const data = [
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ],
    [ /* 请使用用户的真实数据数组替换此处 */ ]
];
function renderItem(params, api) {
  const group = {
    type: 'group',
    children: []
  };
  let coordDims = ['x', 'y'];
  for (let baseDimIdx = 0; baseDimIdx < 2; baseDimIdx++) {
    let otherDimIdx = 1 - baseDimIdx;
    let encode = params.encode;
    let baseValue = api.value(encode[coordDims[baseDimIdx]][0]);
    let param = [];
    param[baseDimIdx] = baseValue;
    param[otherDimIdx] = api.value(encode[coordDims[otherDimIdx]][1]);
    let highPoint = api.coord(param);
    param[otherDimIdx] = api.value(encode[coordDims[otherDimIdx]][2]);
    let lowPoint = api.coord(param);
    let halfWidth = 5;
    var style = api.style({
      stroke: api.visual('color'),
      fill: undefined
    });
    group.children.push(
      {
        type: 'line',
        transition: ['shape'],
        shape: makeShape(
          baseDimIdx,
          highPoint[baseDimIdx] - halfWidth,
          highPoint[otherDimIdx],
          highPoint[baseDimIdx] + halfWidth,
          highPoint[otherDimIdx]
        ),
        style: style
      },
      {
        type: 'line',
        transition: ['shape'],
        shape: makeShape(
          baseDimIdx,
          highPoint[baseDimIdx],
          highPoint[otherDimIdx],
          lowPoint[baseDimIdx],
          lowPoint[otherDimIdx]
        ),
        style: style
      },
      {
        type: 'line',
        transition: ['shape'],
        shape: makeShape(
          baseDimIdx,
          lowPoint[baseDimIdx] - halfWidth,
          lowPoint[otherDimIdx],
          lowPoint[baseDimIdx] + halfWidth,
          lowPoint[otherDimIdx]
        ),
        style: style
      }
    );
  }
  function makeShape(baseDimIdx, base1, value1, base2, value2) {
    var shape = {};
    shape[coordDims[baseDimIdx] + '1'] = base1;
    shape[coordDims[1 - baseDimIdx] + '1'] = value1;
    shape[coordDims[baseDimIdx] + '2'] = base2;
    shape[coordDims[1 - baseDimIdx] + '2'] = value2;
    return shape;
  }
  return group;
}
option = {
  tooltip: {},
  legend: {
    data: ['bar', 'error'],
    top: 15
  },
  dataZoom: [
    {
      type: 'slider'
    },
    {
      type: 'inside'
    }
  ],
  grid: {
    top: 60
  },
  xAxis: {},
  yAxis: {},
  series: [
    {
      type: 'scatter',
      name: 'error',
      data: data,
      dimensions: dimensions,
      encode: {
        x: 2,
        y: 1,
        tooltip: [ /* 请使用用户的真实数据数组替换此处 */ ],
        itemName: 0
      },
      itemStyle: {
        color: '#77bef7'
      }
    },
    {
      type: 'custom',
      name: 'error',
      renderItem: renderItem,
      dimensions: dimensions,
      encode: {
        x: [2, 3, 4],
        y: [1, 5, 6],
        tooltip: [ /* 请使用用户的真实数据数组替换此处 */ ],
        itemName: 0
      },
      data: data,
      z: 100
    }
  ]
};
```

