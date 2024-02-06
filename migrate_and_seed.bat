@echo off
python manage.py migrate
for %%I in (fixtures\administration\seed\*.json) do (
    echo Seeding %%~nxI
    python manage.py loaddata fixtures\administration\seed\%%~nxI
    echo Seeding completed for %%~nxI
)
