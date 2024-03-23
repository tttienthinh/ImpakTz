<script>
  import { BeaconWallet } from "@taquito/beacon-wallet";
  import { NetworkType } from "@airgap/beacon-types";
  import { TezosToolkit } from "@taquito/taquito";

  const rpcUrl = "https://ghostnet.ecadinfra.com";
  const Tezos = new TezosToolkit(rpcUrl);
  const contractAddress = "KT1GoCja6hoW5dEJuXWhVD94o1kKhrDvKQ69";

  let wallet;
  let address;

  let create_car_address;
  let add_verified_address;
  let change_owner_address;
  let add_data_address;
  let add_data_text;
/*

  let balance;
  let bankBalance;

  let depositAmount = 1;
  let depositButtonActive = false;
  let depositButtonLabel = "Deposit";

  let withdrawButtonActive = true;
  let withdrawButtonLabel = "Withdraw";
*/
  const connectWallet = async () => {
    const newWallet = new BeaconWallet({
      name: "Simple dApp tutorial",
      network: {
        type: NetworkType.GHOSTNET,
      },
    });
    await newWallet.requestPermissions();
    address = await newWallet.getPKH();
    // await getWalletBalance(address);
    // await getBankBalance(address);
    wallet = newWallet;
    // depositButtonActive = true;
  };

  const disconnectWallet = () => {
    wallet.client.clearActiveAccount();
    wallet = undefined;
  };

const create_car = async () => {
  Tezos.setWalletProvider(wallet);
  const contract = await Tezos.wallet.at(contractAddress);
  const operation = await contract.methods
    .create_car(create_car_address)
    .send();
  create_car_address = "";
  console.log(`Waiting for ${operation.opHash} to be confirmed...`);
  await operation.confirmation(2);
  console.log(
    `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
  );
};

const add_verified = async () => {
  Tezos.setWalletProvider(wallet);
  const contract = await Tezos.wallet.at(contractAddress);
  const operation = await contract.methods
    .add_verified(add_verified_address)
    .send();
  add_verified_address = "";
  console.log(`Waiting for ${operation.opHash} to be confirmed...`);
  await operation.confirmation(2);
  console.log(
    `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
  );
};

const change_owner = async () => {
  Tezos.setWalletProvider(wallet);
  const contract = await Tezos.wallet.at(contractAddress);
  const operation = await contract.methods
    .change_owner(change_owner_address)
    .send();
    change_owner_address = "";
  console.log(`Waiting for ${operation.opHash} to be confirmed...`);
  await operation.confirmation(2);
  console.log(
    `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
  );
};

const add_data = async () => {
  Tezos.setWalletProvider(wallet);
  const contract = await Tezos.wallet.at(contractAddress);
  const operation = await contract.methods
    .add_data(add_data_address, add_data_text)
    .send();
    add_data_address = "";
    add_data_text = "";
  console.log(`Waiting for ${operation.opHash} to be confirmed...`);
  await operation.confirmation(2);
  console.log(
    `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
  );
};


/*
  const getWalletBalance = async (walletAddress) => {
    const balanceMutez = await Tezos.tz.getBalance(walletAddress);
    balance = balanceMutez.div(1000000).toFormat(2);
  };

  const getBankBalance = async (walletAddress) => {
    const contract = await Tezos.wallet.at(contractAddress);
    const storage = await contract.storage();
    const balanceMutez = await storage.get(walletAddress);
    bankBalance = isNaN(balanceMutez) ? 0 : balanceMutez / 1000000;
  };

  const deposit = async () => {
    depositButtonActive = false;
    depositButtonLabel = "Depositing...";

    Tezos.setWalletProvider(wallet);
    const contract = await Tezos.wallet.at(contractAddress);
    const transactionParams = await contract.methods
      .deposit()
      .toTransferParams({
        amount: depositAmount,
      });
    const estimate = await Tezos.estimate.transfer(transactionParams);

    const operation = await Tezos.wallet
      .transfer({
        ...transactionParams,
        ...estimate,
      })
      .send();

    console.log(`Waiting for ${operation.opHash} to be confirmed...`);

    await operation.confirmation(2);

    console.log(
      `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
    );

    await getWalletBalance(address);
    await getBankBalance(address);
    depositButtonActive = true;
    depositButtonLabel = "Deposit";
  };

  const withdraw = async () => {
    withdrawButtonActive = false;
    withdrawButtonLabel = "Withdrawing...";

    Tezos.setWalletProvider(wallet);
    const contract = await Tezos.wallet.at(contractAddress);

    const transactionParams = await contract.methods
      .withdraw()
      .toTransferParams();
    const estimate = await Tezos.estimate.transfer(transactionParams);

    const operation = await Tezos.wallet
      .transfer({
        ...transactionParams,
        ...estimate,
      })
      .send();

    console.log(`Waiting for ${operation.opHash} to be confirmed...`);

    await operation.confirmation(2);

    console.log(
      `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
    );

    await getWalletBalance(address);
    await getBankBalance(address);
    withdrawButtonActive = true;
    withdrawButtonLabel = "Withdraw";
  };
  */
</script>

<main>
  <h1>ImpakTz</h1>

  <div class="card">
    {#if wallet}
    <div>
      <input type="text"  bind:value={create_car_address} >
      <button on:click={create_car}>
        Create Car
      </button>
    </div>
    <div>
      <input type="text"  bind:value={add_verified_address} >
      <button on:click={add_verified}>
        Add Verified Account
      </button>
    </div>
    <div>
      <input type="text"  bind:value={change_owner_address} >
      <button on:click={change_owner}>
        Change Owner
      </button>
    </div>
    <div>
      <input type="text"  bind:value={add_data_address} >
      <input type="text"  bind:value={add_data_text} >
      <button on:click={add_data}>
        Add Data
      </button>
    </div>
   <!--
      <p>The address of the connected wallet is {address}.</p>
      <p>Its balance in tez is {balance}.</p>
      <p>Its balance in the bank is {bankBalance}.</p>
      <p>
        To get tez, go to <a
          href="https://faucet.ghostnet.teztnets.xyz/"
          target="_blank"
        >
          https://faucet.ghostnet.teztnets.xyz/
        </a>.
      </p>
      <p>
        Deposit tez:
        <input type="number" bind:value={depositAmount} min="1" max="100" />
        <input type="range" bind:value={depositAmount} min="1" max="100" />
        <button on:click={deposit} disabled={!depositButtonActive}>
          {depositButtonLabel}
        </button>
      </p>
      <p>
        Withdraw tez:
        <button on:click={withdraw} disabled={!withdrawButtonActive}>
          {withdrawButtonLabel}
        </button>
      </p>
      <p>
        <button on:click={disconnectWallet}> Disconnect wallet </button>
      </p>
   --> 
    {:else}
      <button on:click={connectWallet}> Connect wallet </button>
    {/if}
  </div>
</main>

<style>
</style>
