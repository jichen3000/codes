# Web SSH Commands Help

This tool helps you run the commands on Linux or Fortigate by SSH.

## Tips

1. You can input 'repeat' times to run commands many times.
2. In the 'Commands History', you will see all results of the commands which have been run. By clicking the 'Restore' button, you can restore the previouse setting. By clicking the log link, you can see the result.



3. supports !sleep seconds

   Example for Fortiagte commands:

   ```
   config global
   exe time
   !sleep 10
   end
   ```

   !sleep 10 will sleep 10 seconds before run the command  'end', and this sleep command would not run on the Fortigate, but on my server side.

