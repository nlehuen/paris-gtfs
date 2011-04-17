if exist "transitfeed\.svn" (
    svn up transitfeed
) else (
    rmdir /s /q transitfeed
    svn co http://googletransitdatafeed.googlecode.com/svn/trunk/python/transitfeed/
)