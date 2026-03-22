## 图表类型：三维折线图 - 正交投影 (Line3D - Orthographic Projection)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var data = [];
// Parametric curve
for (var t = 0; t < 25; t += 0.001) {
  var x = (1 + 0.25 * Math.cos(75 * t)) * Math.cos(t);
  var y = (1 + 0.25 * Math.cos(75 * t)) * Math.sin(t);
  var z = t + 2.0 * Math.sin(75 * t);
  data.push([x, y, z]);
}
console.log(data.length);
option = {
  tooltip: {},
  backgroundColor: '#fff',
  visualMap: {
    show: false,
    dimension: 2,
    min: 0,
    max: 30,
    inRange: {
      color: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  },
  xAxis3D: {
    type: 'value'
  },
  yAxis3D: {
    type: 'value'
  },
  zAxis3D: {
    type: 'value'
  },
  grid3D: {
    viewControl: {
      projection: 'orthographic'
    }
  },
  series: [
    {
      type: 'line3D',
      data: data,
      lineStyle: {
        width: 4
      }
    }
  ]
};
```

