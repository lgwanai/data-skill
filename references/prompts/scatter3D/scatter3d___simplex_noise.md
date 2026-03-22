## 图表类型：三维散点图 - 单纯形噪声 (Scatter3D - Simplex Noise)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getScript(CDN_PATH + 'simplex-noise@2.4.0/simplex-noise.js').done(
  function () {
    var noise = new SimplexNoise(Math.random);
    function generateData(theta, min, max) {
      var data = [];
      for (var i = 0; i <= 20; i++) {
        for (var j = 0; j <= 20; j++) {
          for (var k = 0; k <= 20; k++) {
            var value = noise.noise3D(i / 10, j / 10, k / 10);
            valMax = Math.max(valMax, value);
            valMin = Math.min(valMin, value);
            data.push([i, j, k, value * 2 + 4]);
          }
        }
      }
      return data;
    }
    var valMin = Infinity;
    var valMax = -Infinity;
    var data = generateData(2, -5, 5);
    console.log(valMin, valMax);
    myChart.setOption(
      (option = {
        visualMap: {
          show: false,
          min: 2,
          max: 6,
          inRange: {
            symbolSize: [0.5, 25],
            color: [ /* 请使用用户的真实数据数组替换此处 */ ],
            colorAlpha: [0.2, 1]
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
          axisLine: {
            lineStyle: { color: '#fff' }
          },
          axisPointer: {
            lineStyle: { color: '#fff' }
          },
          viewControl: {
            // autoRotate: true
          }
        },
        series: [
          {
            type: 'scatter3D',
            data: data
          }
        ]
      })
    );
  }
);
```

