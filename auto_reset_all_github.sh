
#!/bin/bash
#
#
#會強制del 所有Server嘅File  然後拉取最新git 所有都係main
#之後再nginx reload
#為咗減輕服務器負擔 Set咗用 crontab 每15分鐘行一次 即係話每15分鐘最多先會運行呢一個program  所以更新最快都要15分鐘


git fetch origin
git reset --hard origin/main
nginx -s reload
