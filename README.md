## Expensify Integration

Integrate Expensify to ERPNext

### Pre-requisites

You have installed and setup Frappe, Bench and ERPNext.

Easiest way to setup is to use virtualbox and the production image. 
https://erpnext.org/download

## Get started

Use these commands to install the integration using bench.

```sh
bench get-app https://github.com/Ion-Mobility-Infra/expensify_integration.git
bench --site site1.local install-app expensify_integration

```

### Frappe setup

Login into the frappe site. 
Add API key, API secret from https://www.expensify.com/tools/integrations/
Add in your default expense approver and default account

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

## License

MIT
