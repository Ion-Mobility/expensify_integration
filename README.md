[![CircleCI](https://circleci.com/gh/Ion-Mobility-Infra/expensify_integration/tree/main.svg?style=shield)](https://circleci.com/gh/Ion-Mobility-Infra/expensify_integration/tree/main)

## Expensify Integration

Integrate Expensify to ERPNext

### Pre-requisites

You have installed and setup Frappe, Bench and ERPNext.

Easiest way to setup is to use virtualbox and the production image. 
https://erpnext.org/download

## Get started

1. Use these commands to install the integration using bench.

```sh
bench get-app https://github.com/Ion-Mobility-Infra/expensify_integration.git
bench --site site1.local install-app expensify_integration
```
2. Login into the frappe site.
3. Ensure your employees are set up such that their full name in Expensify and ERPNext are the same.
4. Set up expense claims accounts inside ERPNext so that they match Expensify's categories exactly.
![ERPNext categories](https://user-images.githubusercontent.com/9346641/117965882-de69cd80-b355-11eb-9163-a9a6eef67591.png)
5. Add API key, API secret from https://www.expensify.com/tools/integrations/
6. Add in your default expense approver and default account

<img width="911" alt="screenshot_expensify_integration" src="https://user-images.githubusercontent.com/9346641/117952869-297ce400-b348-11eb-882f-041d5c7f3c9b.png">

### Hints for development

#### Developer mode
Use developer mode so that the doctype can be automatically generated and saved.
```sh
bench --site site1.local set-config  --global developer_mode 1
```
Ensure the 'Custom?' option is switched off when modifying DocTypes. 

#### Enable cron jobs for ERPNext
```sh
bench --site site1.local scheduler enable
bench --site site1.local scheduler resume
```

#### Re-install app
If settings don't seem to change while developing Frappe apps, you can try to re-install the app again 
```sh 
bench install-app expensify_integration
```
## License

MIT
