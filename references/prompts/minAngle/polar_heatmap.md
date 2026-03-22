## 图表类型：极坐标热力图（自定义系列） (Polar Heatmap)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// prettier-ignore
const hours = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const days = [ /* 请使用用户的真实数据数组替换此处 */ ];
// prettier-ignore
const data = [ /* 请使用用户的真实数据数组替换此处 */ ];
const maxValue = data.reduce(function (max, item) {
  return Math.max(max, item[2]);
}, -Infinity);
option = {
  legend: {
    data: ['Punch Card']
  },
  polar: {},
  tooltip: {},
  visualMap: {
    type: 'continuous',
    min: 0,
    max: maxValue,
    top: 'middle',
    dimension: 2,
    calculable: true
  },
  angleAxis: {
    type: 'category',
    data: hours,
    boundaryGap: false,
    splitLine: {
      show: true,
      lineStyle: {
        color: '#ddd',
        type: 'dashed'
      }
    },
    axisLine: {
      show: false
    }
  },
  radiusAxis: {
    type: 'category',
    data: days,
    z: 100
  },
  series: [
    {
      name: 'Punch Card',
      type: 'custom',
      coordinateSystem: 'polar',
      renderItem: function (params, api) {
        var values = [api.value(0), api.value(1)];
        var coord = api.coord(values);
        var size = api.size([1, 1], values);
        return {
          type: 'sector',
          shape: {
            cx: params.coordSys.cx,
            cy: params.coordSys.cy,
            r0: coord[2] - size[0] / 2,
            r: coord[2] + size[0] / 2,
            startAngle: -(coord[3] + size[1] / 2),
            endAngle: -(coord[3] - size[1] / 2)
          },
          style: api.style({
            fill: api.visual('color')
          })
        };
      },
      data: data
    }
  ]
};
```

