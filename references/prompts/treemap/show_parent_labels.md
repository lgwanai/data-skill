## 图表类型：显示父层级标签 (Show Parent Labels)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/data/disk.tree.json]**:
```json
数据是一个数组 (Array)，共 71 项。单项结构示例：
[
  {
    "value": 40,
    "name": "Accessibility",
    "path": "Accessibility"
  },
  {
    "value": 180,
    "name": "Accounts",
    "path": "Accounts",
    "children": [
      {
        "value": 76,
        "name": "Access",
        "path": "Accounts/Access",
        "children": [
          {
            "value": 12,
            "name": "DefaultAccessPlugin.bundle",
            "path": "Accounts/Access/DefaultAccessPlugin.bundle"
          },
          {
            "value": 28,
            "name": "FacebookAccessPlugin.bundle",
            "path": "Accounts/Access/FacebookAccessPlugin.bundle"
          },
          {
            "value": 20,
            "name": "LinkedInAccessPlugin.bundle",
            "path": "Accounts/Access/LinkedInAccessPlugin.bundle"
          },
          {
            "value": 16,
            "name": "TencentWeiboAccessPlugin.bundle",
            "path": "Accounts/Access/TencentWeiboAccessPlugin.bundle"
          }
        ]
      },
      {
        "value": 92,
        "name": "Authentication",
        "path": "Accounts/Authentication",
        "children": [
          {
            "value": 24,
            "name": "FacebookAuthenticationPlugin.bundle",
            "path": "Accounts/Authentication/FacebookAuthenticationPlugin.bundle"
          },
          {
            "value": 16,
            "name": "LinkedInAuthenticationPlugin.bundle",
            "path": "Accounts/Authentication/LinkedInAuthenticationPlugin.bundle"
          },
          {
            "value": 20,
            "name": "TencentWeiboAuthenticationPlugin.bundle",
            "path": "Accounts/Authentication/TencentWeiboAuthenticationPlugin.bundle"
          },
          {
            "value": 16,
            "name": "TwitterAuthenticationPlugin.bundle",
            "path": "Accounts/Authentication/TwitterAuthenticationPlugin.bundle"
          },
          {
            "value": 16,
            "name": "WeiboAuthenticationPlugin.bundle",
            "path": "Accounts/Authentication/WeiboAuthenticationPlugin.bundle"
          }
        ]
      },
      {
        "value": 12,
        "name": "Notification",
        "path": "Accounts/Notification",
        "children": [
          {
            "value": 12,
            "name": "SPAAccountsNotificationPlugin.bundle",
            "path": "Accounts/Notification/SPAAccountsNotificationPlugin.bundle"
          }
        ]
      }
    ]
  }
]
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
myChart.showLoading();
$.get(ROOT_PATH + '/data/asset/data/disk.tree.json', function (diskData) {
  myChart.hideLoading();
  function getLevelOption() {
    return [
      {
        itemStyle: {
          borderColor: '#777',
          borderWidth: 0,
          gapWidth: 1
        },
        upperLabel: {
          show: false
        }
      },
      {
        itemStyle: {
          borderColor: '#555',
          borderWidth: 5,
          gapWidth: 1
        },
        emphasis: {
          itemStyle: {
            borderColor: '#ddd'
          }
        }
      },
      {
        colorSaturation: [0.35, 0.5],
        itemStyle: {
          borderWidth: 5,
          gapWidth: 1,
          borderColorSaturation: 0.6
        }
      }
    ];
  }
  myChart.setOption(
    (option = {
      title: {
        text: 'Disk Usage',
        left: 'center'
      },
      tooltip: {
        formatter: function (info) {
          var value = info.value;
          var treePathInfo = info.treePathInfo;
          var treePath = [];
          for (var i = 1; i < treePathInfo.length; i++) {
            treePath.push(treePathInfo[i].name);
          }
          return [
            '<div class="tooltip-title">' +
              echarts.format.encodeHTML(treePath.join('/')) +
              '</div>',
            'Disk Usage: ' + echarts.format.addCommas(value) + ' KB'
          ].join('');
        }
      },
      series: [
        {
          name: 'Disk Usage',
          type: 'treemap',
          visibleMin: 300,
          label: {
            show: true,
            formatter: '{b}'
          },
          upperLabel: {
            show: true,
            height: 30
          },
          itemStyle: {
            borderColor: '#fff'
          },
          levels: getLevelOption(),
          data: diskData
        }
      ]
    })
  );
});
```

