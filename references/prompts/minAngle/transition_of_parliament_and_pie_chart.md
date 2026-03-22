## 图表类型：自定义议会图与饼图过渡动画 (Transition of Parliament and Pie Chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const data = [
  { value: 800, name: 'A' },
  { value: 635, name: 'B' },
  { value: 580, name: 'C' },
  { value: 484, name: 'D' },
  { value: 300, name: 'E' },
  { value: 200, name: 'F' }
];
const defaultPalette = [ /* 请使用用户的真实数据数组替换此处 */ ];
const radius = ['30%', '80%'];
const pieOption = {
  series: [
    {
      type: 'pie',
      id: 'distribution',
      radius: radius,
      label: {
        show: false
      },
      universalTransition: true,
      animationDurationUpdate: 1000,
      data: data
    }
  ]
};
const parliamentOption = (function () {
  let sum = data.reduce(function (sum, cur) {
    return sum + cur.value;
  }, 0);
  let angles = [];
  let startAngle = -Math.PI / 2;
  let curAngle = startAngle;
  data.forEach(function (item) {
    angles.push(curAngle);
    curAngle += (item.value / sum) * Math.PI * 2;
  });
  angles.push(startAngle + Math.PI * 2);
  function parliamentLayout(startAngle, endAngle, totalAngle, r0, r1, size) {
    let rowsCount = Math.ceil((r1 - r0) / size);
    let points = [];
    let r = r0;
    for (let i = 0; i < rowsCount; i++) {
      // Recalculate size
      let totalRingSeatsNumber = Math.round((totalAngle * r) / size);
      let newSize = (totalAngle * r) / totalRingSeatsNumber;
      for (
        let k = Math.floor((startAngle * r) / newSize) * newSize;
        k < Math.floor((endAngle * r) / newSize) * newSize - 1e-6;
        k += newSize
      ) {
        let angle = k / r;
        let x = Math.cos(angle) * r;
        let y = Math.sin(angle) * r;
        points.push([x, y]);
      }
      r += size;
    }
    return points;
  }
  return {
    series: {
      type: 'custom',
      id: 'distribution',
      data: data,
      coordinateSystem: undefined,
      universalTransition: true,
      animationDurationUpdate: 1000,
      renderItem: function (params, api) {
        var idx = params.dataIndex;
        var viewSize = Math.min(api.getWidth(), api.getHeight());
        var r0 = ((parseFloat(radius[0]) / 100) * viewSize) / 2;
        var r1 = ((parseFloat(radius[1]) / 100) * viewSize) / 2;
        var cx = api.getWidth() * 0.5;
        var cy = api.getHeight() * 0.5;
        var size = viewSize / 50;
        var points = parliamentLayout(
          angles[idx],
          angles[idx + 1],
          Math.PI * 2,
          r0,
          r1,
          size + 3
        );
        return {
          type: 'group',
          children: points.map(function (pt) {
            return {
              type: 'circle',
              autoBatch: true,
              shape: {
                cx: cx + pt[0],
                cy: cy + pt[1],
                r: size / 2
              },
              style: {
                fill: defaultPalette[idx % defaultPalette.length]
              }
            };
          })
        };
      }
    }
  };
})();
let currentOption = (option = pieOption);
setInterval(function () {
  currentOption = currentOption === pieOption ? parliamentOption : pieOption;
  myChart.setOption(currentOption);
}, 2000);
```

