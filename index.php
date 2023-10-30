<html>
<head>
  <title>Run my Python files</title>
</head>
<body>
  <button onclick="<?php echo shell_exec('python test.py'); ?>">Run Python Script</button>
</body>
</html>