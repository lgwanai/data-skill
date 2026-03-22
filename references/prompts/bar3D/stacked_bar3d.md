## 图表类型：三维堆叠柱状图 (Stacked Bar3D)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getScript(CDN_PATH + 'simplex-noise@2.4.0/simplex-noise.js').done(
  function () {
    function generateData() {
      var data = [];
      var noise = new SimplexNoise(Math.random);
      for (var i = 0; i <= 10; i++) {
        for (var j = 0; j <= 10; j++) {
          var value = noise.noise2D(i / 5, j / 5);
          data.push([i, j, value * 2 + 4]);
        }
      }
      return data;
    }
    var series = [];
    for (var i = 0; i < 10; i++) {
      series.push({
        type: 'bar3D',
        data: generateData(),
        stack: 'stack',
        shading: 'lambert',
        emphasis: {
          label: {
            show: false
          }
        }
      });
    }
    myChart.setOption({
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
          // autoRotate: true
        },
        light: {
          main: {
            shadow: true,
            quality: 'ultra',
            intensity: 1.5
          }
        }
      },
      series: series
    });
  }
);
```

