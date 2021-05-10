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

Insert screenshots, to be continued

### Hints for development

Use developer mode so that the doctype can be automatically generated and saved.
```sh
bench --site site1.local set-config  --global developer_mode 1
```
Ensure the 'Custom?' option is switched off when modifying DocTypes. 


## License

MIT
