if [ -e /home/root/jobber/.jobber ]
then
	cd /bin/bash
else
	jobber init
	cat jobber.txt > /home/root/.jobber
fi
